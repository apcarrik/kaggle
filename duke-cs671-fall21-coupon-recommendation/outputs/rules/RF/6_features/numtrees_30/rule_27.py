def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[4]>0.0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[5]<=2:
						return 'True'
					elif obj[5]>2:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>7:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[1]>1:
				# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=0.0:
		return 'False'
	else: return 'False'
