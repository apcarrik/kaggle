def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[6]<=2.0:
		# {"feature": "Occupation", "instances": 79, "metric_value": 0.9663, "depth": 2}
		if obj[4]<=20:
			# {"feature": "Coupon", "instances": 77, "metric_value": 0.9556, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 67, "metric_value": 0.9279, "depth": 4}
				if obj[8]>1:
					# {"feature": "Bar", "instances": 39, "metric_value": 0.9766, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Education", "instances": 35, "metric_value": 0.9518, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Time", "instances": 24, "metric_value": 0.9799, "depth": 7}
							if obj[1]>0:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.9928, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 19, "metric_value": 0.9819, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>2:
							# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[0]>1:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>2.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>2:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>2:
								return 'False'
							elif obj[1]<=2:
								return 'True'
							else: return 'True'
						elif obj[0]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[8]<=1:
					# {"feature": "Bar", "instances": 28, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Time", "instances": 18, "metric_value": 0.5033, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]>1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]>20:
			return 'False'
		else: return 'False'
	elif obj[6]>2.0:
		return 'True'
	else: return 'True'
