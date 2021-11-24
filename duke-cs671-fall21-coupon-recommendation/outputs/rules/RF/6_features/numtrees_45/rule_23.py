def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=9:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>9:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1.0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0.0:
						return 'True'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'True'
