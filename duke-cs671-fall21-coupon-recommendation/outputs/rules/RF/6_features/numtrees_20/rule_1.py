def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.896, "depth": 2}
		if obj[3]<=21:
			# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.8691, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Education", "instances": 30, "metric_value": 0.8366, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Passanger", "instances": 27, "metric_value": 0.8767, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[4]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]>21:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Passanger", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[2]<=4:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[3]<=14:
					# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				elif obj[3]>14:
					return 'False'
				else: return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
