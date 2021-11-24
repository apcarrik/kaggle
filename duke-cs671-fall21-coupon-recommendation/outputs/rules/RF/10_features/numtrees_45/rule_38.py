def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=17:
		# {"feature": "Direction_same", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[8]<=0:
			# {"feature": "Education", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[3]>0:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5]<=2.0:
						return 'False'
					elif obj[5]>2.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[6]<=3.0:
						return 'True'
					elif obj[6]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[8]>0:
			return 'False'
		else: return 'False'
	elif obj[4]>17:
		return 'True'
	else: return 'True'
