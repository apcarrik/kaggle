def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 64, "metric_value": 0.9972, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coupon", "instances": 48, "metric_value": 0.995, "depth": 3}
			if obj[2]>2:
				# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=12:
					# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.7919, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[1]>0:
							# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[5]<=2.0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[5]>2.0:
									return 'False'
								else: return 'False'
							elif obj[8]>2:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]>12:
					return 'False'
				else: return 'False'
			elif obj[2]<=2:
				# {"feature": "Bar", "instances": 24, "metric_value": 0.9799, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[4]>5:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[1]>0:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[8]>2:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>2.0:
							return 'False'
						else: return 'False'
					elif obj[4]<=5:
						return 'False'
					else: return 'False'
				elif obj[5]<=0.0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]>5:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]>0:
									return 'False'
								elif obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>2:
										return 'False'
									elif obj[8]<=2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]>2.0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[4]<=5:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>2:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[8]>1:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=4:
							return 'False'
						elif obj[4]>4:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]<=1:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=6:
						return 'True'
					elif obj[4]>6:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Time", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=7:
				# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[6]>0.0:
					return 'True'
				elif obj[6]<=0.0:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>7:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]>0.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
