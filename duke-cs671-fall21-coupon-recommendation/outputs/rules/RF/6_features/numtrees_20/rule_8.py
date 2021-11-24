def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[3]<=19:
		# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.9109, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Coupon", "instances": 36, "metric_value": 0.9641, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 26, "metric_value": 0.8905, "depth": 4}
				if obj[5]>1:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[5]<=1:
					# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[2]>1:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]<=2:
						return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]>19:
		# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[2]>0:
			return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
