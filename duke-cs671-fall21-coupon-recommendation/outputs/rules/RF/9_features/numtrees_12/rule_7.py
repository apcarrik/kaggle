def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[4]>2.1129432661168055:
		# {"feature": "Passanger", "instances": 69, "metric_value": 0.9877, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 42, "metric_value": 0.9934, "depth": 3}
			if obj[3]<=4:
				# {"feature": "Coupon", "instances": 40, "metric_value": 0.9837, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 34, "metric_value": 1.0, "depth": 5}
					if obj[8]<=1:
						# {"feature": "Bar", "instances": 21, "metric_value": 0.9587, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Direction_same", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[7]>0:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[6]<=1.0:
										return 'True'
									elif obj[6]>1.0:
										return 'False'
									else: return 'False'
								elif obj[7]<=0:
									# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[6]<=1.0:
										return 'False'
									elif obj[6]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[5]<=0.0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[7]<=0:
								return 'True'
							elif obj[7]>0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>1:
						# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[1]<=1:
								return 'False'
							elif obj[1]>1:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]>4:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Bar", "instances": 27, "metric_value": 0.8256, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[2]>1:
					# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[1]>0:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[8]>1:
							# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>2.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>3:
								return 'False'
							else: return 'False'
						elif obj[8]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=3:
							return 'True'
						elif obj[3]>3:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]<=2.1129432661168055:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=0:
						return 'True'
					elif obj[3]>0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>1.0:
								return 'False'
							elif obj[6]<=1.0:
								return 'True'
							else: return 'True'
						elif obj[5]>0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	else: return 'True'
