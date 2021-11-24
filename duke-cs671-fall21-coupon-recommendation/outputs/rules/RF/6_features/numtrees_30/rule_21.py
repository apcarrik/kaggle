def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]>4:
		# {"feature": "Education", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[2]>0:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[5]>1:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	elif obj[3]<=4:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[0]>0:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[1]>2:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
