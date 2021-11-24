def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[19]>1:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[5]>1:
			# {"feature": "Weather", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Driving_to", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>30:
						return 'True'
					elif obj[3]<=30:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>1:
				return 'True'
			else: return 'True'
		elif obj[5]<=1:
			return 'False'
		else: return 'False'
	elif obj[19]<=1:
		# {"feature": "Weather", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[2]<=1:
			return 'True'
		elif obj[2]>1:
			return 'False'
		else: return 'False'
	else: return 'True'
