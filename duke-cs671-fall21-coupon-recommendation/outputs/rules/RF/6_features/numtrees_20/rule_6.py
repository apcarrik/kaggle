def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Occupation", "instances": 47, "metric_value": 0.9839, "depth": 2}
		if obj[3]<=21:
			# {"feature": "Passanger", "instances": 45, "metric_value": 0.971, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 33, "metric_value": 0.9993, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 5}
					if obj[5]>1:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]<=1:
						# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[5]>1:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1]>2:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[1]<=2:
						return 'True'
					else: return 'True'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>21:
			return 'False'
		else: return 'False'
	elif obj[4]>2.0:
		return 'True'
	else: return 'True'
