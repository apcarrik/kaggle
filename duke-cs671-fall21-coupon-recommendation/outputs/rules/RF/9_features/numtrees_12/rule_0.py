def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[2]>0:
		# {"feature": "Time", "instances": 72, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Passanger", "instances": 49, "metric_value": 0.8631, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Bar", "instances": 30, "metric_value": 0.971, "depth": 4}
				if obj[5]<=3.0:
					# {"feature": "Distance", "instances": 28, "metric_value": 0.9403, "depth": 5}
					if obj[8]<=1:
						# {"feature": "Direction_same", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=1:
									# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]>1:
										return 'False'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								elif obj[3]>1:
									return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[8]>1:
						# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[3]>1:
							# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[4]<=7:
								return 'False'
							elif obj[4]>7:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>1.0:
									return 'True'
								elif obj[6]<=1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[3]<=1:
							# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=7:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[4]>7:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[5]>3.0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 19, "metric_value": 0.4855, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[4]<=12:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					elif obj[4]>12:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[4]>1:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[8]<=1:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[5]>2.0:
								return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[8]>1:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Passanger", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
