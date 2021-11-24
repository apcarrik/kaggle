def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Restaurant20to50", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[9]>-1.0:
		# {"feature": "Bar", "instances": 123, "metric_value": 0.9827, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Occupation", "instances": 66, "metric_value": 0.9024, "depth": 3}
			if obj[6]<=8:
				# {"feature": "Age", "instances": 41, "metric_value": 0.6594, "depth": 4}
				if obj[4]>0:
					# {"feature": "Passanger", "instances": 33, "metric_value": 0.4395, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 22, "metric_value": 0.5746, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[2]<=3:
										return 'True'
									elif obj[2]>3:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=2.0:
											return 'False'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[2]>0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[10]<=0:
											return 'True'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>2:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>8:
				# {"feature": "Education", "instances": 25, "metric_value": 0.9896, "depth": 4}
				if obj[5]>0:
					# {"feature": "Distance", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[2]>1:
							# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[4]>1:
									return 'True'
								elif obj[4]<=1:
									return 'False'
								else: return 'False'
							elif obj[8]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=0:
							return 'True'
						elif obj[3]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=0.0:
			# {"feature": "Coupon", "instances": 57, "metric_value": 0.9944, "depth": 3}
			if obj[2]>0:
				# {"feature": "Age", "instances": 48, "metric_value": 0.995, "depth": 4}
				if obj[4]>1:
					# {"feature": "Distance", "instances": 38, "metric_value": 0.998, "depth": 5}
					if obj[11]>1:
						# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 6}
						if obj[6]>4:
							# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[8]<=3.0:
								# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[1]>3:
										return 'False'
									else: return 'False'
								elif obj[5]>2:
									return 'True'
								else: return 'True'
							elif obj[8]>3.0:
								return 'False'
							else: return 'False'
						elif obj[6]<=4:
							# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[5]<=3:
									return 'False'
								elif obj[5]>3:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5]<=1:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[5]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]<=1:
						# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6]>1:
										return 'False'
									elif obj[6]<=1:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>2:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=0:
								# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=4:
									return 'True'
								elif obj[6]>4:
									return 'False'
								else: return 'False'
							elif obj[0]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=2:
						return 'True'
					elif obj[5]>2:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[11]>1:
							return 'False'
						elif obj[11]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[9]<=-1.0:
		return 'False'
	else: return 'False'
