def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[4]<=1:
			# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[7]>0:
				# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[14]<=0.0:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=1:
						return 'False'
					elif obj[9]>1:
						return 'True'
					else: return 'True'
				elif obj[14]>0.0:
					return 'True'
				else: return 'True'
			elif obj[7]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]>1:
			# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[8]<=2:
				return 'True'
			elif obj[8]>2:
				# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[9]<=1:
					return 'False'
				elif obj[9]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[1]>1:
		return 'True'
	else: return 'True'
