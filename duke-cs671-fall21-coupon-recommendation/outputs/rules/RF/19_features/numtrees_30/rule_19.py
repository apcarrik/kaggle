def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[11]>1:
			# {"feature": "Age", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[7]>2:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[18]<=2:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[10]>1:
						# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[12]<=3:
								return 'True'
							elif obj[12]>3:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[17]<=0:
									return 'False'
								elif obj[17]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[10]<=1:
						return 'True'
					else: return 'True'
				elif obj[18]>2:
					return 'False'
				else: return 'False'
			elif obj[7]<=2:
				return 'False'
			else: return 'False'
		elif obj[11]<=1:
			return 'True'
		else: return 'True'
	elif obj[3]>2:
		# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[18]<=2:
			# {"feature": "Income", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[12]>2:
				return 'True'
			elif obj[12]<=2:
				# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=55:
					return 'True'
				elif obj[2]>55:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[18]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
