def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[19]<=2:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.8813, "depth": 2}
		if obj[5]<=3:
			# {"feature": "Coupon_validity", "instances": 23, "metric_value": 0.6666, "depth": 3}
			if obj[6]>0:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[8]<=4:
						return 'True'
					elif obj[8]>4:
						# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=0:
							return 'False'
						elif obj[0]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[14]>1.0:
					# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]>0:
						return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[5]>3:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[12]<=14:
				return 'False'
			elif obj[12]>14:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=1:
					return 'True'
				elif obj[4]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[19]>2:
		return 'False'
	else: return 'False'
