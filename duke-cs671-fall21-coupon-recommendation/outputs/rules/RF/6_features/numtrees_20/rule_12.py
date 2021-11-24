def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[3]<=17:
		# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.9971, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Coupon", "instances": 43, "metric_value": 0.9808, "depth": 3}
			if obj[1]>2:
				# {"feature": "Passanger", "instances": 28, "metric_value": 0.9963, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]>1:
						return 'True'
					elif obj[5]<=1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>2:
							return 'False'
						elif obj[2]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=2:
				# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	elif obj[3]>17:
		return 'True'
	else: return 'True'
