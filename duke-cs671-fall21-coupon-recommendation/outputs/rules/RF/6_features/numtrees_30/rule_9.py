def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>0:
		# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[4]<=1.0:
				return 'False'
			elif obj[4]>1.0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]>2:
					return 'False'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[1]>3:
				# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[3]<=5:
			return 'True'
		elif obj[3]>5:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]>2:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					elif obj[1]<=2:
						return 'True'
					else: return 'True'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
