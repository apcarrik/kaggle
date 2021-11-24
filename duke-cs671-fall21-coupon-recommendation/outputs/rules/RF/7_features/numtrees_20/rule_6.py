def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 38, "metric_value": 0.9819, "depth": 2}
		if obj[3]>5:
			# {"feature": "Education", "instances": 21, "metric_value": 0.7919, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[6]<=1:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[0]>2:
						return 'True'
					elif obj[0]<=2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>1:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]<=5:
			# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[2]>1:
				# {"feature": "Passanger", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>3:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=1:
							return 'True'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=3:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
