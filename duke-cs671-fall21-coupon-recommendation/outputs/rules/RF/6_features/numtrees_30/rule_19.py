def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]>0:
		# {"feature": "Education", "instances": 27, "metric_value": 0.9183, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[3]>7:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]>1:
						return 'True'
					elif obj[5]<=1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
