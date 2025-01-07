from django.shortcuts import render
from django.db.models import Count
from app.models import AdminMaster
from app.models import Subject
from app.models import Class
from app.models import Faculty
from app.models import Day
from app.models import Students
from app.models import Attendance

from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
from django.core.mail import send_mail
import cv2
import os
import numpy as np
import json
from django.utils import timezone
import datetime
import calendar
from django.db.models import Q


def adminAdmin(request):
    return render(request, "admin/admin.html")


def days(request):
    return render(request, "admin/days.html")


def notifications(request):
    return render(request, "admin/notifications.html")


def subject(request):
    return render(request, "admin/subject.html")


def faculty(request):
    return render(request, "admin/faculty.html")


def students(request):
    return render(request, "admin/students.html")


def classes(request):
    return render(request, "admin/class.html")


def attendance(request):
    return render(request, "admin/attendance.html")


def report(request):
    return render(request, "admin/report.html")


def userStudents(request):
    if Students.objects.filter(
        us_email=request.POST["txtEmail"], us_status="0"
    ).exists():
        return HttpResponse("1")
    else:
        lclID = Students.objects.count()
        status = "0"

        Students.objects.create(
            us_name=request.POST["txtName"],
            us_email=request.POST["txtEmail"],
            us_mobile=request.POST["txtMobile"],
            us_address=request.POST["txtAddress"],
            us_password=request.POST["txtPassword"],
            us_status=status,
        )

        return HttpResponse()


def loginValidate(request):
    if (
        AdminMaster.objects.filter(
            ad_email=request.POST["txtEmail"],
            ad_password=request.POST["txtPassword"],
            ad_status=0,
        ).count()
        > 0
    ):
        jsonData = AdminMaster.objects.filter(
            ad_email=request.POST["txtEmail"]
        ).values()
        data = list(jsonData)
        dictValue = data[0]
        request.session["email"] = dictValue["ad_email"]
        request.session["name"] = dictValue["ad_name"]

        return HttpResponse("Admin")
    else:
        return HttpResponse("0")


# AdminMaster
def adminDetails(request):
    if request.POST["action"] == "add":
        AdminMaster.objects.create(
            ad_name=request.POST["txtName"],
            ad_email=request.POST["txtEmail"],
            ad_mobile=request.POST["txtMobileNo"],
            ad_password=request.POST["txtPassword"],
            ad_role=request.POST["selRole"],
        )
    elif request.POST["action"] == "getData":
        data = AdminMaster.objects.filter(ad_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = AdminMaster.objects.filter(ad_id=request.POST["id"]).update(
            ad_name=request.POST["txtName1"],
            ad_email=request.POST["txtEmail1"],
            ad_mobile=request.POST["txtMobileNo1"],
        )

    elif request.POST["action"] == "delete":
        data = AdminMaster.objects.filter(ad_id=request.POST["id"]).update(
            ad_status="1"
        )

    return HttpResponse()


# Days
def days_details(request):
    if request.POST["action"] == "add":
        Day.objects.create(
            day_name=request.POST["txtName"],
        )
    elif request.POST["action"] == "getData":
        data = Day.objects.filter(day_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = Day.objects.filter(day_id=request.POST["id"]).update(
            day_name=request.POST["txtName1"],
        )

    elif request.POST["action"] == "delete":
        data = Day.objects.filter(day_id=request.POST["id"]).update(day_status="1")

    return HttpResponse()


# Subject
def subject_details(request):
    if request.POST["action"] == "add":
        Subject.objects.create(
            su_name=request.POST["txtName"],
        )
    elif request.POST["action"] == "getData":
        data = Subject.objects.filter(su_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = Subject.objects.filter(su_id=request.POST["id"]).update(
            su_name=request.POST["txtName1"],
        )

    elif request.POST["action"] == "delete":
        data = Subject.objects.filter(su_id=request.POST["id"]).update(su_status="1")

    return HttpResponse()


# Faculty
def faculty_details(request):
    if request.POST["action"] == "add":
        Faculty.objects.create(
            fc_name=request.POST["txtName"],
            fc_mobile=request.POST["txtMobileNo"],
            fc_email=request.POST["txtEmail"],
        )
    elif request.POST["action"] == "getData":
        data = Faculty.objects.filter(fc_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = Faculty.objects.filter(fc_id=request.POST["id"]).update(
            fc_name=request.POST["txtName1"],
            fc_email=request.POST["txtEmail1"],
            fc_mobile=request.POST["txtMobileNo1"],
        )

    elif request.POST["action"] == "delete":
        data = Faculty.objects.filter(fc_id=request.POST["id"]).update(fc_status="1")

    return HttpResponse()


# Student
def student_details(request):
    if request.POST["action"] == "add":

        if Students.objects.filter(
            us_usn=request.POST["txtUsn"], us_status="0"
        ).count():
            return HttpResponse("10")
        else:

            # Load Haar cascade for face detection
            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )

            # Initialize webcam
            camera = cv2.VideoCapture(0)

            def capture_faces(student_id):
                student_folder = os.path.join(
                    settings.STATICFILES_DIRS[0], "dataset", str(student_id)
                )
                if not os.path.exists(student_folder):
                    os.makedirs(student_folder)

                i = 0
                while i < 20:
                    input("Press Enter to capture")
                    ret, frame = camera.read()
                    if not ret:
                        print("Error: Failed to capture frame")
                        break

                    # Convert frame to grayscale for face detection
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Detect faces in the frame
                    faces = face_cascade.detectMultiScale(
                        gray, scaleFactor=1.3, minNeighbors=5
                    )

                    if len(faces) == 0:
                        print("No face detected. Please try again.")
                        continue

                    # Save only the first detected face
                    x, y, w, h = faces[0]
                    face_roi = frame[y : y + h, x : x + w]

                    cv2.imwrite(os.path.join(student_folder, f"{i+1}.png"), face_roi)
                    print(f"Face {i+1} captured for student {student_id}")
                    i += 1

            # Input student ID
            student_id = request.POST["txtUsn"]
            capture_faces(student_id)

            # Release webcam
            camera.release()
            Students.objects.create(
                us_usn=request.POST["txtUsn"],
                us_name=request.POST["txtName"],
                us_email=request.POST["txtEmail"],
                us_mobile=request.POST["txtMobileNo"],
                us_address=request.POST["txtAddress"],
                us_parent_email=request.POST["txtParentEmail"],
            )
    elif request.POST["action"] == "getData":
        data = Students.objects.filter(us_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = Students.objects.filter(us_id=request.POST["id"]).update(
            us_usn=request.POST["txtUsn1"],
            us_name=request.POST["txtName1"],
            us_email=request.POST["txtEmail1"],
            us_mobile=request.POST["txtMobileNo1"],
            us_address=request.POST["txtAddress1"],
            us_parent_email=request.POST["txtParentEmail1"],
        )

    elif request.POST["action"] == "delete":
        data = Students.objects.filter(us_id=request.POST["id"]).update(us_status="1")

    return HttpResponse()


# Class
def class_details(request):
    if request.POST["action"] == "add":
        Class.objects.create(
            cl_time=request.POST["txtTime"],
            cl_day_id=request.POST["selDays"],
            cl_faculty_id=request.POST["selFaculty"],
            cl_subject_id=request.POST["selSubject"],
        )
    elif request.POST["action"] == "getData":
        data = Class.objects.filter(cl_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = Class.objects.filter(cl_id=request.POST["id"]).update(
            cl_time=request.POST["txtTime1"],
            cl_day_id=request.POST["selDays1"],
            cl_faculty_id=request.POST["selFaculty1"],
            cl_subject_id=request.POST["selSubject1"],
        )

    elif request.POST["action"] == "delete":
        data = Class.objects.filter(cl_id=request.POST["id"]).update(cl_status="1")

    return HttpResponse()


# Attendance
def attendance_details(request):
    if request.POST["action"] == "getData":
        queryset = Attendance.objects.filter(at_status="0").values()
        modified_data = []

        for item in queryset:
            try:
                class_obj = Class.objects.get(cl_id=item["at_class_id"])
                student_obj = Students.objects.get(us_usn=item["at_student_id"])
                modified_item = {
                    "us_name": student_obj.us_name,
                    "us_usn": student_obj.us_usn,
                    "cl_day_id": class_obj.cl_day_id,
                    "cl_time": class_obj.cl_time,
                    "cl_subject_id": class_obj.cl_subject_id,
                }
                modified_data.append(modified_item)
            except (Class.DoesNotExist, Students.DoesNotExist):
                pass
        values = JsonResponse(modified_data, safe=False)

        return values

    return HttpResponse()


def report_details(request):
    if request.POST["action"] == "getData":
        selMonth = int(request.POST.get("selMonth"))
        selYear = int(request.POST.get("selYear"))

        # Get the number of days in the selected month
        num_days = calendar.monthrange(selYear, selMonth)[1]

        # Define the start and end dates for the selected month and year
        start_date = f"{selYear}-{selMonth:02d}-01"
        end_date = f"{selYear}-{selMonth:02d}-{num_days}"

        # Filter attendance data for the selected month and year
        queryset = (
            Attendance.objects.filter(
                Q(at_status="0"),
                Q(at_date_time__date__gte=start_date),
                Q(at_date_time__date__lte=end_date),
            )
            .values("at_student_id", "at_class_id")
            .annotate(total_attendance=Count("at_student_id"))
        )

        student_attendance = {}
        for item in queryset:
            student_id = item["at_student_id"]
            total_attendance = item["total_attendance"]
            class_id = item["at_class_id"]
            if student_id not in student_attendance:
                student_attendance[student_id] = {}
            student_attendance[student_id][class_id] = total_attendance

        # Fetch student details from Students table
        students_queryset = Students.objects.filter(
            us_usn__in=student_attendance.keys()
        ).values("us_usn", "us_name")

        # Fetch class details from Class table
        class_queryset = Class.objects.filter(
            cl_id__in=[
                class_id
                for student_data in student_attendance.values()
                for class_id in student_data.keys()
            ]
        ).values("cl_id", "cl_subject_id")

        class_subject_map = {
            cls["cl_id"]: cls["cl_subject_id"] for cls in class_queryset
        }

        modified_data = []
        for student in students_queryset:
            us_usn = student["us_usn"]
            us_name = student["us_name"]
            student_classes = student_attendance.get(us_usn, {})
            for class_id, total_attendance in student_classes.items():
                class_subject_id = class_subject_map.get(class_id)
                modified_item = {
                    "us_name": us_name,
                    "us_usn": us_usn,
                    "class_subject_id": class_subject_id,
                    "total_attendance": total_attendance,
                }
                modified_data.append(modified_item)

        return JsonResponse(modified_data, safe=False)


def userLoginValidate(request):
    if Students.objects.filter(
        us_email=request.POST["txtEmail"],
        us_password=request.POST["txtPassword"],
        us_status="0",
    ).exists():
        products_json = Students.objects.filter(
            us_email=request.POST["txtEmail"]
        ).values()
        data = list(products_json)
        dictValue = data[0]
        request.session["web_email"] = dictValue["us_email"]
        request.session["web_address"] = dictValue["us_address"]
        return HttpResponse("1")
    else:
        return HttpResponse("0")


def adminLogin(request):
    return render(request, "admin_login.html")


def checkUserSession(request):
    if "web_email" in request.session:
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def webLogout(request):
    request.session.delete()
    return render(request, "web/index.html")


def Logout(request):
    request.session.delete()
    return render(request, "admin_login.html")


def camera(request):
    return render(request, "web/camera.html")


def send_notifications(request):
    current_date = timezone.now().date()

    # Filter attendance data for the current date
    attendance_data = Attendance.objects.filter(
        at_date_time__date=current_date
    ).values()

    # Group attendance data by day ID
    attendance_by_class = {}
    for attendance in attendance_data:
        if attendance["at_class_id"] not in attendance_by_class:
            attendance_by_class[attendance["at_class_id"]] = []
        attendance_by_class[attendance["at_class_id"]].append(attendance)

    # Send emails
    for class_id, attendances in attendance_by_class.items():
        # Get the faculty ID for this class from the Class table
        class_obj = Class.objects.get(cl_id=class_id)
        faculty_id = class_obj.cl_faculty_id
        class_day = class_obj.cl_day_id
        class_subject = class_obj.cl_subject_id

        # Get the faculty name from the Faculty table
        faculty_obj = Faculty.objects.get(fc_name=faculty_id)
        faculty_name = faculty_obj.fc_name

        # Prepare the email content
        subject = f"Attendance Notification for Class Day {class_day}, Subject {class_subject}"

        faculty_email = faculty_obj.fc_email  # Assuming Faculty has an email field

        for attendance in attendances:
            body = ""
            body += f"Faculty Name: {faculty_name}\n"
            body += "Attendance Details:\n\n"

            # Get the parent's email for the student
            student_obj = Students.objects.get(us_usn=attendance["at_student_id"])
            parent_email = student_obj.us_parent_email

            # Add attendance details to the email body
            body += f"Student ID: {attendance['at_student_id']}\n"
            body += f"Attendance Status: Present\n\n"

            # Send the email using Django's send_mail function and configured settings
            send_mail(subject, body, settings.EMAIL_HOST_USER, [parent_email])

        # Send email to faculty with overall attendance details
        overall_body = ""
        overall_body += f"Faculty Name: {faculty_name}\n"
        overall_body += "Overall Attendance Details:\n\n"

        for attendance in attendances:
            overall_body += f"Student ID: {attendance['at_student_id']}\n"
            overall_body += f"Attendance Status: Present\n\n"

    send_mail(subject, overall_body, settings.EMAIL_HOST_USER, [faculty_email])

    current_date = timezone.now().date()

    # Get all students from the Students table
    students = Students.objects.all()

    # Get attendance data for the current date
    attendance_data = Attendance.objects.filter(
        at_date_time__date=current_date
    ).values_list("at_student_id", flat=True)

    # Find students who are in the Students table but not in the Attendance table
    absent_students = students.exclude(us_usn__in=attendance_data)

    # Send emails for absent students
    for student in absent_students:
        parent_email = student.us_parent_email
        student_id = student.us_usn

        # Prepare the email content for parent
        subject_parent = f"Attendance Notification for Student ID {student_id}"
        body_parent = f"Your child with Student ID {student_id} was marked absent for class on {current_date}. Please contact the College for further details."

        # Send email to parent using Django's send_mail function and configured settings
        send_mail(subject_parent, body_parent, settings.EMAIL_HOST_USER, [parent_email])

        # Get the classes that the student is enrolled in based on the Attendance table
        student_classes = Class.objects.filter(
            cl_id__in=Attendance.objects.filter(
                at_student_id=student_id, at_date_time__date=current_date
            ).values_list("at_class_id", flat=True)
        )

        for student_class in student_classes:
            faculty_email = student_class.cl_faculty_id.fc_email
            class_id = student_class.cl_id

            # Prepare the email content for faculty
            subject_faculty = f"Attendance Notification for Class ID {class_id}"
            body_faculty = f"Student with ID {student_id} was marked absent for your class on {current_date}. Please follow up with the student."

            # Send email to faculty using Django's send_mail function and configured settings
            send_mail(
                subject_faculty, body_faculty, settings.EMAIL_HOST_USER, [faculty_email]
            )

    return HttpResponse("Notifications sent successfully.")


def trainModel(request):
    image_folder = "static/dataset"  # Assuming the dataset is located in static/dataset
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    def train_recognizer(images, labels):
        recognizer.train(images, np.array(labels))
        model_path = os.path.join("static", "face_recognizer_model.yml")
        recognizer.save(model_path)

    images = []
    labels = []
    student_id_mapping = {}
    current_id = 0

    for subfolder in os.listdir(image_folder):
        print(subfolder)
        subfolder_path = os.path.join(image_folder, subfolder)
        if os.path.isdir(subfolder_path):
            current_id += 1
            student_id_mapping[subfolder] = current_id
            for filename in os.listdir(subfolder_path):
                path = os.path.join(subfolder_path, filename)
                img = cv2.imread(path)
                if img is not None:
                    label = current_id
                    label = subfolder[-3 : len(subfolder)]
                    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    images.append(gray_img)
                    labels.append(int(label))

    train_recognizer(images, labels)
    return HttpResponse(0)


def classAttendance(request):
    # Load the trained LBPH face recognizer model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    model_path = os.path.join("static", "face_recognizer_model.yml")
    recognizer.read(model_path)

    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Initialize the webcam
    camera = cv2.VideoCapture(0)

    # Create a mapping between student IDs and their corresponding folder names
    student_id_mapping = {}
    data = Students.objects.filter(us_status="0").values()
    data = list(data)

    student_id_mapping = {
        int(student["us_usn"][-3:]): student["us_name"] for student in data
    }

    while True:
        # Capture a frame from the webcam
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Iterate through detected faces
        for x, y, w, h in faces:
            # Draw a rectangle around the face region
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Crop the face region for recognition
            face_roi = gray[y : y + h, x : x + w]

            # Perform face recognition
            label, confidence = recognizer.predict(face_roi)
            # print(label)

            # Map the numeric label to the corresponding student ID (folder name)
            student_id = student_id_mapping.get(label, "Unknown")

            # Display the recognized student ID and confidence level
            # text = f"Student ID: {student_id}, Confidence: {confidence:.2f}"
            text = f"Student: {student_id}"
            cv2.putText(
                frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2
            )

            today_day = datetime.datetime.now().strftime("%A")

            # Get current time (e.g., "10:30")
            current_time = datetime.datetime.now().strftime("%H")
            current_datetime = timezone.now()

            # Filter data from the Class table based on today's full day name and current time
            data = Class.objects.filter(
                cl_status="0", cl_day_id=today_day, cl_time=current_time
            ).values()
            data = list(data)
            # print(data)

            if data:

                studentUSN = "2JR21CS" + str(label)
                # print(studentUSN)
                cl_id = data[0]["cl_id"]

                data1 = Attendance.objects.filter(
                    at_student_id=studentUSN,
                    at_class_id=cl_id,
                    at_date_time__date=current_datetime.date(),
                ).values()
                data1 = list(data1)

                if not data1:

                    Attendance.objects.create(
                        at_student_id=studentUSN,
                        at_class_id=cl_id,
                    )

        # Display the frame with face detection and recognition
        cv2.imshow("Face Recognition", frame)

        # Wait for 'q' key to quit the program
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera and close all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()
    return HttpResponse()
