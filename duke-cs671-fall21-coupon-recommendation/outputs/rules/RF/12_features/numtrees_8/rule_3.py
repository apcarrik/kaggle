def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Direction_same", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[10]<=0:
		# {"feature": "Coffeehouse", "instances": 105, "metric_value": 0.9947, "depth": 2}
		if obj[8]>1.0:
			# {"feature": "Time", "instances": 54, "metric_value": 0.9841, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 42, "metric_value": 0.9403, "depth": 4}
				if obj[11]>1:
					# {"feature": "Occupation", "instances": 27, "metric_value": 0.9911, "depth": 5}
					if obj[6]<=14:
						# {"feature": "Coupon", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[0]>1:
								# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[4]>0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[5]<=2:
												return 'True'
											elif obj[5]>2:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[7]>2.0:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[9]>-1.0:
									return 'False'
								elif obj[9]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[5]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>14:
						return 'True'
					else: return 'True'
				elif obj[11]<=1:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=1.0:
							# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						elif obj[9]>1.0:
							return 'True'
						else: return 'True'
					elif obj[6]>4:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[4]>2:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[11]<=2:
						return 'True'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				elif obj[4]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[8]<=1.0:
			# {"feature": "Distance", "instances": 51, "metric_value": 0.9183, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Age", "instances": 38, "metric_value": 0.9819, "depth": 4}
				if obj[4]>0:
					# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 1.0, "depth": 5}
					if obj[9]>0.0:
						# {"feature": "Coupon", "instances": 25, "metric_value": 0.971, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 8}
								if obj[6]>2:
									# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[0]>1:
												return 'True'
											elif obj[0]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]>3:
											return 'False'
										else: return 'False'
									elif obj[7]>0.0:
										return 'True'
									else: return 'True'
								elif obj[6]<=2:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>1:
										return 'False'
									elif obj[0]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[5]>2:
								return 'False'
							else: return 'False'
						elif obj[2]>3:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[6]<=11:
								return 'False'
							elif obj[6]>11:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=2:
										return 'True'
									elif obj[1]>2:
										return 'False'
									else: return 'False'
								elif obj[7]>0.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[9]<=0.0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[6]>2:
							return 'True'
						elif obj[6]<=2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[11]>2:
				# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[10]>0:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.5746, "depth": 2}
		if obj[6]>5:
			return 'True'
		elif obj[6]<=5:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[8]>0.0:
					return 'True'
				elif obj[8]<=0.0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
