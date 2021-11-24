def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Gender", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[5]>0:
		# {"feature": "Weather", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[15]<=2.0:
				# {"feature": "Education", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[9]<=3:
					return 'True'
				elif obj[9]>3:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]>2.0:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	elif obj[5]<=0:
		# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[12]<=2.0:
			# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[7]<=1:
				return 'False'
			elif obj[7]>1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>3:
					return 'False'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
