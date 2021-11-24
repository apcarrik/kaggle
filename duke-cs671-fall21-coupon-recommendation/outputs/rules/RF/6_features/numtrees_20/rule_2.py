def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.9495, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Occupation", "instances": 35, "metric_value": 0.8981, "depth": 3}
			if obj[3]>4:
				# {"feature": "Education", "instances": 25, "metric_value": 0.971, "depth": 4}
				if obj[2]>1:
					# {"feature": "Passanger", "instances": 18, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]>1:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=4:
				# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2.0:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>2:
					return 'True'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
