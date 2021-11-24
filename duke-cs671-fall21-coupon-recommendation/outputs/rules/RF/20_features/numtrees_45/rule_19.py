def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[12]<=11:
			# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[7]>0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]<=0:
				return 'False'
			else: return 'False'
		elif obj[12]>11:
			return 'True'
		else: return 'True'
	elif obj[11]>1:
		# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=55:
				return 'True'
			elif obj[3]>55:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
