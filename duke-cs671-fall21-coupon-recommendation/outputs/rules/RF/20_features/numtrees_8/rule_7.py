def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9621, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon_validity", "instances": 93, "metric_value": 0.8953, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Income", "instances": 49, "metric_value": 0.688, "depth": 3}
			if obj[13]>2:
				# {"feature": "Bar", "instances": 33, "metric_value": 0.4395, "depth": 4}
				if obj[14]<=1.0:
					return 'True'
				elif obj[14]>1.0:
					# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[4]>0:
						# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[18]<=0:
							return 'True'
						elif obj[18]>0:
							return 'False'
						else: return 'False'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[13]<=2:
				# {"feature": "Driving_to", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=0:
					# {"feature": "Gender", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>0:
					# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]<=55:
						return 'False'
					elif obj[3]>55:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[7]<=0:
							return 'False'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Maritalstatus", "instances": 44, "metric_value": 0.994, "depth": 3}
			if obj[9]<=1:
				# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.9789, "depth": 4}
				if obj[17]>0.0:
					# {"feature": "Coffeehouse", "instances": 37, "metric_value": 0.9953, "depth": 5}
					if obj[15]>1.0:
						# {"feature": "Gender", "instances": 23, "metric_value": 0.8865, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[12]<=7:
								# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[11]>0:
									# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]>30:
											return 'False'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[11]<=0:
									return 'True'
								else: return 'True'
							elif obj[12]>7:
								return 'False'
							else: return 'False'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					elif obj[15]<=1.0:
						# {"feature": "Children", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[16]<=1.0:
								# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=55:
									return 'False'
								elif obj[3]>55:
									return 'True'
								else: return 'True'
							elif obj[16]>1.0:
								return 'True'
							else: return 'True'
						elif obj[10]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[17]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[9]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Age", "instances": 34, "metric_value": 0.9774, "depth": 2}
		if obj[8]>1:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.7732, "depth": 3}
			if obj[12]>5:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[17]>0.0:
					# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Temperature", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[3]<=55:
							# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[16]>2.0:
								# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									return 'False'
								else: return 'False'
							elif obj[16]<=2.0:
								return 'False'
							else: return 'False'
						elif obj[3]>55:
							return 'True'
						else: return 'True'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				elif obj[17]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[12]<=5:
				return 'False'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[15]<=3.0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[7]>0:
						return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]>3.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
