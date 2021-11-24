def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 61, "metric_value": 0.967, "depth": 2}
		if obj[3]>5:
			# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.9961, "depth": 3}
			if obj[4]<=3.0:
				# {"feature": "Passanger", "instances": 38, "metric_value": 0.9819, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 27, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=4:
						# {"feature": "Direction_same", "instances": 26, "metric_value": 0.8905, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 17, "metric_value": 0.7871, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>4:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[6]>1:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]>0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>3.0:
				return 'True'
			else: return 'True'
		elif obj[3]<=5:
			# {"feature": "Distance", "instances": 20, "metric_value": 0.469, "depth": 3}
			if obj[6]>1:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Education", "instances": 24, "metric_value": 0.7383, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[3]<=10:
				return 'False'
			elif obj[3]>10:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[3]>2:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						return 'False'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[3]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
