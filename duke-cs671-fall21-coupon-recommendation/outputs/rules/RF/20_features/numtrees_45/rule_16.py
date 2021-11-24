def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[5]>1:
		# {"feature": "Driving_to", "instances": 15, "metric_value": 0.3534, "depth": 2}
		if obj[0]<=1:
			return 'True'
		elif obj[0]>1:
			return 'False'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[8]<=3:
			return 'False'
		elif obj[8]>3:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]>1:
				return 'True'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
