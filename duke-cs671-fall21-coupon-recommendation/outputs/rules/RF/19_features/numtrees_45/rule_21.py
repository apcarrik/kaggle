def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]<=4:
		# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[4]>1:
				# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[8]>0:
					return 'True'
				elif obj[8]<=0:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[7]>4:
		# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[2]>30:
			return 'True'
		elif obj[2]<=30:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
