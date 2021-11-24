def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 92, "metric_value": 0.9945, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coffeehouse", "instances": 74, "metric_value": 0.9995, "depth": 3}
			if obj[6]<=3.0:
				# {"feature": "Bar", "instances": 68, "metric_value": 0.9975, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Time", "instances": 39, "metric_value": 0.9418, "depth": 5}
					if obj[1]>0:
						# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.8366, "depth": 6}
						if obj[7]>1.0:
							# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 7}
							if obj[4]>8:
								# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[3]>1:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=1:
									return 'False'
								else: return 'False'
							elif obj[4]<=8:
								return 'True'
							else: return 'True'
						elif obj[7]<=1.0:
							# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 7}
							if obj[4]>1:
								return 'False'
							elif obj[4]<=1:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[9]<=1:
									return 'False'
								elif obj[9]>1:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[4]>2:
								return 'True'
							elif obj[4]<=2:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=0.0:
					# {"feature": "Time", "instances": 29, "metric_value": 0.9576, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 25, "metric_value": 0.9896, "depth": 6}
						if obj[4]<=14:
							# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9799, "depth": 7}
							if obj[7]>-1.0:
								# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Distance", "instances": 21, "metric_value": 0.9852, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9928, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										return 'True'
									else: return 'True'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							elif obj[7]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[4]>14:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]>3.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[4]<=11:
						# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[1]>0:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[9]>1:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[6]>0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=1:
									return 'False'
								else: return 'False'
							elif obj[5]>0.0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[4]>11:
						return 'True'
					else: return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[7]>1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 35, "metric_value": 0.7755, "depth": 2}
		if obj[4]<=21:
			# {"feature": "Distance", "instances": 33, "metric_value": 0.684, "depth": 3}
			if obj[9]>1:
				# {"feature": "Coupon", "instances": 25, "metric_value": 0.795, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.5436, "depth": 5}
					if obj[6]<=1.0:
						return 'True'
					elif obj[6]>1.0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>3:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]>0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]>2:
							return 'True'
						elif obj[1]<=2:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0.0:
								return 'False'
							elif obj[5]>0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=1:
				return 'True'
			else: return 'True'
		elif obj[4]>21:
			return 'False'
		else: return 'False'
	else: return 'True'
