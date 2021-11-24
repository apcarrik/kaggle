def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 41, "metric_value": 0.9262, "depth": 1}
	if obj[5]>1:
		# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.8338, "depth": 2}
		if obj[9]>0:
			# {"feature": "Bar", "instances": 25, "metric_value": 0.9427, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.8865, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Income", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[13]>2:
						# {"feature": "Distance", "instances": 15, "metric_value": 0.8366, "depth": 6}
						if obj[20]<=1:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[12]<=7:
								# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[7]<=0:
									return 'True'
								elif obj[7]>0:
									# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[12]>7:
								# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2]<=0:
									return 'False'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[20]>1:
							return 'True'
						else: return 'True'
					elif obj[13]<=2:
						# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]>55:
							return 'False'
						elif obj[3]<=55:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[15]>2.0:
					return 'True'
				else: return 'True'
			elif obj[14]>3.0:
				return 'False'
			else: return 'False'
		elif obj[9]<=0:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[6]>0:
			return 'False'
		elif obj[6]<=0:
			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[7]<=0:
				return 'True'
			elif obj[7]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
