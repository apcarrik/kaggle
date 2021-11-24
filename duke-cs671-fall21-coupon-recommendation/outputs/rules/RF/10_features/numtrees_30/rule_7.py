def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 2}
		if obj[4]>2:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3228, "depth": 3}
			if obj[7]>0.0:
				return 'True'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[4]<=2:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[5]<=0.0:
					return 'False'
				elif obj[5]>0.0:
					return 'True'
				else: return 'True'
			elif obj[3]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0.0:
					return 'False'
				elif obj[6]<=0.0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[7]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
