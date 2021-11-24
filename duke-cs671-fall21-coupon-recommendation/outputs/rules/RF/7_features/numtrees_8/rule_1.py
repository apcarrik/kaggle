def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[1]>0:
		# {"feature": "Education", "instances": 102, "metric_value": 0.9864, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 56, "metric_value": 0.9963, "depth": 3}
			if obj[3]<=10:
				# {"feature": "Distance", "instances": 39, "metric_value": 0.9957, "depth": 4}
				if obj[6]>1:
					# {"feature": "Passanger", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[4]>0.0:
								return 'True'
							elif obj[4]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>1.0:
								return 'False'
							elif obj[4]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=2.0:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=1:
					# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[4]<=0.0:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>10:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Occupation", "instances": 46, "metric_value": 0.8865, "depth": 3}
			if obj[3]<=11:
				# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.7897, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Distance", "instances": 34, "metric_value": 0.8338, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Passanger", "instances": 30, "metric_value": 0.7838, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 23, "metric_value": 0.8281, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>2:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]>11:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]<=0:
						return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Passanger", "instances": 25, "metric_value": 0.5294, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Direction_same", "instances": 21, "metric_value": 0.2762, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=6:
					return 'False'
				elif obj[3]>6:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]>4:
				return 'False'
			elif obj[3]<=4:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
