def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[16]>1.0:
		# {"feature": "Time", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[12]<=14:
				# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[19]<=2:
						# {"feature": "Gender", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[7]>0:
							# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[13]<=4:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]>2:
									return 'True'
								elif obj[8]<=2:
									return 'False'
								else: return 'False'
							elif obj[13]>4:
								return 'False'
							else: return 'False'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					elif obj[19]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[12]>14:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Temperature", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[3]<=55:
				return 'True'
			elif obj[3]>55:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[16]<=1.0:
		return 'False'
	else: return 'False'
