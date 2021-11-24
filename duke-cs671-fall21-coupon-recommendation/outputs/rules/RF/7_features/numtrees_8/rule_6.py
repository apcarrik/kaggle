def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[3]<=8.007874015748031:
		# {"feature": "Coupon", "instances": 79, "metric_value": 0.938, "depth": 2}
		if obj[1]>1:
			# {"feature": "Education", "instances": 63, "metric_value": 0.8631, "depth": 3}
			if obj[2]>1:
				# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.9518, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Distance", "instances": 25, "metric_value": 0.9988, "depth": 5}
					if obj[6]<=1:
						# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>1:
						# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[6]>1:
						return 'True'
					elif obj[6]<=1:
						# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Distance", "instances": 28, "metric_value": 0.6769, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Passanger", "instances": 27, "metric_value": 0.6052, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.65, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 21, "metric_value": 0.7025, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[0]>0:
				# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>8.007874015748031:
		# {"feature": "Passanger", "instances": 48, "metric_value": 0.9544, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coupon", "instances": 30, "metric_value": 0.7219, "depth": 3}
			if obj[1]>2:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Education", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[6]>1:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
