def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coupon", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Passanger", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
