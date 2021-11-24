def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9692, "depth": 1}
	if obj[5]>1:
		# {"feature": "Occupation", "instances": 139, "metric_value": 0.8839, "depth": 2}
		if obj[12]<=18.586723744890453:
			# {"feature": "Age", "instances": 129, "metric_value": 0.9103, "depth": 3}
			if obj[8]>1:
				# {"feature": "Maritalstatus", "instances": 79, "metric_value": 0.8163, "depth": 4}
				if obj[9]<=1:
					# {"feature": "Coffeehouse", "instances": 63, "metric_value": 0.8832, "depth": 5}
					if obj[15]>0.0:
						# {"feature": "Driving_to", "instances": 45, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coupon_validity", "instances": 36, "metric_value": 0.8113, "depth": 7}
							if obj[6]>0:
								# {"feature": "Income", "instances": 18, "metric_value": 0.9641, "depth": 8}
								if obj[13]<=3:
									# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[11]<=0:
											return 'True'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[13]>3:
									# {"feature": "Carryaway", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[16]>-1.0:
										return 'True'
									elif obj[16]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]<=0:
								# {"feature": "Direction_same", "instances": 18, "metric_value": 0.5033, "depth": 8}
								if obj[19]<=0:
									# {"feature": "Income", "instances": 17, "metric_value": 0.3228, "depth": 9}
									if obj[13]<=5:
										return 'True'
									elif obj[13]>5:
										# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]<=55:
											return 'True'
										elif obj[3]>55:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[19]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[15]<=0.0:
						# {"feature": "Bar", "instances": 18, "metric_value": 0.9911, "depth": 6}
						if obj[14]<=1.0:
							# {"feature": "Driving_to", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[11]<=1:
										# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[2]<=1:
												return 'True'
											elif obj[2]>1:
												return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									elif obj[11]>1:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[14]>1.0:
							# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[13]<=6:
								return 'True'
							elif obj[13]>6:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[9]>1:
					# {"feature": "Education", "instances": 16, "metric_value": 0.3373, "depth": 5}
					if obj[11]<=3:
						return 'True'
					elif obj[11]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]<=1:
				# {"feature": "Carryaway", "instances": 50, "metric_value": 0.9896, "depth": 4}
				if obj[16]>1.0:
					# {"feature": "Time", "instances": 38, "metric_value": 0.8997, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Bar", "instances": 23, "metric_value": 0.7554, "depth": 6}
						if obj[14]<=2.0:
							# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.3373, "depth": 7}
							if obj[9]<=2:
								return 'True'
							elif obj[9]>2:
								return 'False'
							else: return 'False'
						elif obj[14]>2.0:
							# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]>55:
								# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[9]>0:
									return 'True'
								elif obj[9]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]<=55:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>2:
						# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[1]>2:
							# {"feature": "Children", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[10]<=0:
								return 'True'
							elif obj[10]>0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=2:
							# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[16]<=1.0:
					# {"feature": "Temperature", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[3]<=55:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[17]>1.0:
								return 'False'
							elif obj[17]<=1.0:
								# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>1:
									return 'False'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[3]>55:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[12]>18.586723744890453:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Gender", "instances": 65, "metric_value": 0.971, "depth": 2}
		if obj[7]<=0:
			# {"feature": "Coupon_validity", "instances": 34, "metric_value": 0.99, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Income", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[13]>2:
					# {"feature": "Driving_to", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[14]<=1.0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=3:
								return 'False'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[14]>1.0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[13]<=2:
					return 'True'
				else: return 'True'
			elif obj[6]>0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[12]>6:
					return 'False'
				elif obj[12]<=6:
					# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[13]<=4:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[13]>4:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>0:
			# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.7706, "depth": 3}
			if obj[15]<=2.0:
				# {"feature": "Income", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[13]<=4:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[12]<=10:
						return 'False'
					elif obj[12]>10:
						# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]>0:
								return 'True'
							elif obj[8]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[13]>4:
					# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[4]>0:
						# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[8]>1:
							# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[15]>2.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
