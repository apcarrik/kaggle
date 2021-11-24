def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 0.9762, "depth": 1}
	if obj[11]>5:
		# {"feature": "Education", "instances": 80, "metric_value": 0.9995, "depth": 2}
		if obj[10]>1:
			# {"feature": "Income", "instances": 44, "metric_value": 0.9024, "depth": 3}
			if obj[12]>2:
				# {"feature": "Distance", "instances": 27, "metric_value": 0.9911, "depth": 4}
				if obj[18]<=2:
					# {"feature": "Temperature", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[2]>30:
						# {"feature": "Age", "instances": 19, "metric_value": 0.9819, "depth": 6}
						if obj[7]<=5:
							# {"feature": "Time", "instances": 16, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[15]>1.0:
									# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[4]<=2:
										return 'True'
									elif obj[4]>2:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[14]<=3.0:
											return 'True'
										elif obj[14]>3.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[15]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[13]>1.0:
									return 'False'
								elif obj[13]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]>5:
							return 'False'
						else: return 'False'
					elif obj[2]<=30:
						return 'True'
					else: return 'True'
				elif obj[18]>2:
					return 'False'
				else: return 'False'
			elif obj[12]<=2:
				# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.5226, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[7]>2:
						return 'False'
					elif obj[7]<=2:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[10]<=1:
			# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.888, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Coupon", "instances": 30, "metric_value": 0.7219, "depth": 4}
				if obj[4]>0:
					# {"feature": "Maritalstatus", "instances": 29, "metric_value": 0.6632, "depth": 5}
					if obj[8]<=3:
						# {"feature": "Age", "instances": 28, "metric_value": 0.5917, "depth": 6}
						if obj[7]>0:
							# {"feature": "Income", "instances": 23, "metric_value": 0.4262, "depth": 7}
							if obj[12]<=4:
								return 'True'
							elif obj[12]>4:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[15]>2.0:
										return 'False'
									elif obj[15]<=2.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[7]<=0:
							# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]>0:
								# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[18]<=1:
									return 'True'
								elif obj[18]>1:
									return 'False'
								else: return 'False'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>3:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[14]<=0.0:
				# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[7]>0:
					return 'False'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[11]<=5:
		# {"feature": "Restaurantlessthan20", "instances": 47, "metric_value": 0.785, "depth": 2}
		if obj[15]>1.0:
			# {"feature": "Coupon", "instances": 37, "metric_value": 0.878, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Bar", "instances": 29, "metric_value": 0.7355, "depth": 4}
				if obj[13]<=1.0:
					# {"feature": "Time", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[3]>0:
						# {"feature": "Income", "instances": 12, "metric_value": 1.0, "depth": 6}
						if obj[12]>2:
							# {"feature": "Temperature", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[2]>30:
								return 'True'
							elif obj[2]<=30:
								# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]<=2:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[13]>1.0:
					return 'True'
				else: return 'True'
			elif obj[4]>3:
				# {"feature": "Temperature", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]>55:
					return 'False'
				elif obj[2]<=55:
					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=0:
						return 'True'
					elif obj[9]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[15]<=1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
