def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]>0:
		# {"feature": "Passanger", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Temperature", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[2]<=55:
				return 'False'
			elif obj[2]>55:
				# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]>0:
						return 'True'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[10]>0:
				return 'True'
			elif obj[10]<=0:
				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=0:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[11]>3:
			return 'True'
		elif obj[11]<=3:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4]>3:
				return 'False'
			elif obj[4]<=3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
