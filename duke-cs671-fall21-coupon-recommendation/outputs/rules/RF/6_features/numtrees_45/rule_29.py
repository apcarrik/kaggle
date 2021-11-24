def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Education", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[3]>4:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]<=4:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]>2:
				return 'True'
			elif obj[0]<=2:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>6:
					return 'True'
				elif obj[3]<=6:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
