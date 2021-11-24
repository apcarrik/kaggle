def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Education", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[2]>0:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=3:
							return 'True'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]>2:
					return 'True'
				elif obj[1]<=2:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[3]>7:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[4]<=0.0:
				return 'False'
			elif obj[4]>0.0:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
