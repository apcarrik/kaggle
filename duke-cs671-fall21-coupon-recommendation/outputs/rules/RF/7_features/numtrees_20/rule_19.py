def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 34, "metric_value": 0.7871, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Education", "instances": 27, "metric_value": 0.8767, "depth": 3}
			if obj[2]>1:
				# {"feature": "Passanger", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>2.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=0.0:
						return 'True'
					elif obj[4]>0.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>1:
							return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]>7:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[3]<=9:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[6]<=1:
						return 'False'
					elif obj[6]>1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[3]>9:
			return 'False'
		else: return 'False'
	else: return 'False'
