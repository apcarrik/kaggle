def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[1]>2:
		# {"feature": "Occupation", "instances": 33, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=14:
			# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.8498, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Passanger", "instances": 24, "metric_value": 0.7383, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.7732, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>2.0:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1:
						return 'True'
					elif obj[5]>1:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>14:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=2:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[5]>1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=5:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>5:
					return 'False'
				else: return 'False'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[3]<=14:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[3]>14:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
