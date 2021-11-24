def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[5]<=3.0:
		# {"feature": "Coupon", "instances": 120, "metric_value": 0.9992, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 84, "metric_value": 0.9737, "depth": 3}
			if obj[4]<=8.154761904761905:
				# {"feature": "Passanger", "instances": 49, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 38, "metric_value": 0.9268, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Distance", "instances": 35, "metric_value": 0.9518, "depth": 6}
						if obj[8]<=1:
							# {"feature": "Time", "instances": 18, "metric_value": 0.8524, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[6]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[6]>2.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>1:
							# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[6]>2.0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[6]<=1.0:
						return 'True'
					elif obj[6]>1.0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>1:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>8.154761904761905:
				# {"feature": "Direction_same", "instances": 35, "metric_value": 0.9852, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Passanger", "instances": 29, "metric_value": 0.9576, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Time", "instances": 15, "metric_value": 0.7219, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[3]>1:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[8]>2:
										return 'False'
									elif obj[8]<=2:
										return 'False'
									else: return 'False'
								elif obj[3]<=1:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[6]<=0.0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>3:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]<=1:
									return 'True'
								elif obj[8]>1:
									return 'False'
								else: return 'False'
							elif obj[1]<=3:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[1]>2:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[3]>0:
									# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[8]<=2:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[1]<=2:
								# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3]>0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=1:
							return 'True'
						elif obj[8]>1:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 36, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 32, "metric_value": 0.9544, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[4]<=13:
							# {"feature": "Direction_same", "instances": 18, "metric_value": 1.0, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[8]>1:
										return 'False'
									elif obj[8]<=1:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[4]>13:
							return 'True'
						else: return 'True'
					elif obj[6]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]>3.0:
		return 'True'
	else: return 'True'
