def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 22, "metric_value": 0.7732, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coupon", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]<=6:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[3]>6:
						return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[2]<=0:
			return 'True'
		elif obj[2]>0:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=6:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
