def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]>0.0:
		# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[5]<=3.0:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>2:
							return 'True'
						elif obj[3]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[5]>3.0:
			return 'False'
		else: return 'False'
	elif obj[4]<=0.0:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1]>3:
			return 'False'
		elif obj[1]<=3:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
