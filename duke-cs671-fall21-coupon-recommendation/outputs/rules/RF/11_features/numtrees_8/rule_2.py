def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 93, "metric_value": 0.9959, "depth": 2}
		if obj[5]>1.0919568473250694:
			# {"feature": "Coffeehouse", "instances": 77, "metric_value": 0.9793, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Age", "instances": 57, "metric_value": 0.998, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 5}
					if obj[4]>0:
						# {"feature": "Bar", "instances": 31, "metric_value": 0.9812, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[1]>0:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[10]>1:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											return 'True'
										else: return 'True'
									elif obj[10]<=1:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]>0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]>1:
												return 'True'
											elif obj[10]<=1:
												return 'False'
											else: return 'False'
										elif obj[9]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[2]>3:
								# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									return 'False'
								elif obj[1]<=0:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>1.0:
										return 'True'
									elif obj[8]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[6]>1.0:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[9]<=0:
								return 'False'
							elif obj[9]>0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2]>0:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[2]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=0:
						# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Bar", "instances": 18, "metric_value": 0.9641, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 8}
								if obj[10]<=2:
									# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 9}
									if obj[2]>1:
										# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									elif obj[2]<=1:
										return 'False'
									else: return 'False'
								elif obj[10]>2:
									return 'True'
								else: return 'True'
							elif obj[6]>2.0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]>-1.0:
						return 'False'
					elif obj[6]<=-1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=0.0:
				# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0:
					# {"feature": "Age", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[2]>1:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[10]>1:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[6]>0.0:
												return 'False'
											elif obj[6]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											return 'True'
										else: return 'True'
									elif obj[9]>0:
										return 'False'
									else: return 'False'
								elif obj[2]<=1:
									return 'False'
								else: return 'False'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						elif obj[8]>1.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[5]<=1.0919568473250694:
			# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[10]>1:
				# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0:
						return 'True'
					elif obj[4]<=0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Time", "instances": 34, "metric_value": 0.8338, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Education", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[7]>0.0:
					return 'True'
				elif obj[7]<=0.0:
					# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=0.0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]<=3:
								return 'True'
							elif obj[2]>3:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]>0.0:
									return 'True'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]>0.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>2:
				# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'True'
