def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9996, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coupon", "instances": 90, "metric_value": 0.9825, "depth": 2}
		if obj[2]>0:
			# {"feature": "Gender", "instances": 74, "metric_value": 1.0, "depth": 3}
			if obj[3]>0:
				# {"feature": "Age", "instances": 39, "metric_value": 0.9612, "depth": 4}
				if obj[4]>0:
					# {"feature": "Occupation", "instances": 33, "metric_value": 0.994, "depth": 5}
					if obj[7]<=14:
						# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.951, "depth": 6}
						if obj[10]<=1.0:
							# {"feature": "Time", "instances": 16, "metric_value": 0.6962, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 9}
									if obj[8]<=1.0:
										return 'True'
									elif obj[8]>1.0:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9]>0.0:
											return 'True'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]>3:
									# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9]>0.0:
										return 'False'
									elif obj[9]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>3:
								return 'False'
							else: return 'False'
						elif obj[10]>1.0:
							# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[12]>1:
									return 'False'
								elif obj[12]<=1:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=2:
										return 'True'
									elif obj[6]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>14:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[9]<=1.0:
							return 'False'
						elif obj[9]>1.0:
							# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.9518, "depth": 4}
				if obj[9]<=3.0:
					# {"feature": "Bar", "instances": 31, "metric_value": 0.9072, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Occupation", "instances": 27, "metric_value": 0.951, "depth": 6}
						if obj[7]<=19:
							# {"feature": "Age", "instances": 26, "metric_value": 0.9306, "depth": 7}
							if obj[4]>0:
								# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 9}
									if obj[10]>-1.0:
										# {"feature": "Time", "instances": 19, "metric_value": 0.998, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												return 'False'
											else: return 'False'
										elif obj[1]>1:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[6]>3:
									return 'False'
								else: return 'False'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]>19:
							return 'True'
						else: return 'True'
					elif obj[8]>2.0:
						return 'False'
					else: return 'False'
				elif obj[9]>3.0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=6:
						return 'True'
					elif obj[7]>6:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Time", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Age", "instances": 37, "metric_value": 0.8419, "depth": 2}
		if obj[4]>3:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.4395, "depth": 3}
			if obj[7]<=7:
				return 'True'
			elif obj[7]>7:
				# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=3:
			# {"feature": "Children", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[5]>0:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[8]>0.0:
					return 'False'
				elif obj[8]<=0.0:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=0:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[10]<=1.0:
					return 'True'
				elif obj[10]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
