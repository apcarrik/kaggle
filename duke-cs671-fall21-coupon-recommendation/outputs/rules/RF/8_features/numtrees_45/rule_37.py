def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]>2:
						return 'False'
					elif obj[3]<=2:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]>0.0:
					return 'True'
				elif obj[5]<=0.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'False'
		else: return 'False'
	elif obj[4]>1.0:
		return 'True'
	else: return 'True'
