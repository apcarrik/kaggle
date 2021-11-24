def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[3]<=16:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[5]>2:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		elif obj[3]>16:
			return 'False'
		else: return 'False'
	elif obj[2]>2:
		# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
