def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[4]<=14.891453572731104:
		# {"feature": "Bar", "instances": 71, "metric_value": 0.9359, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Education", "instances": 51, "metric_value": 0.8479, "depth": 3}
			if obj[3]>0:
				# {"feature": "Coupon", "instances": 36, "metric_value": 0.9436, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 34, "metric_value": 0.9082, "depth": 5}
					if obj[0]>0:
						# {"feature": "Time", "instances": 31, "metric_value": 0.9383, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[8]<=2:
										return 'True'
									elif obj[8]>2:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[6]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=1.0:
							return 'True'
						elif obj[6]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]>1.0:
			# {"feature": "Coupon", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>2:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[6]>1.0:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[7]<=0:
					return 'False'
				elif obj[7]>0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]>14.891453572731104:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[2]>1:
			# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[8]<=2:
								return 'False'
							elif obj[8]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
