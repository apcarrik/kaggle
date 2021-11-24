def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[5]<=20:
		# {"feature": "Age", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[2]>1:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[8]>0.0:
						return 'True'
					elif obj[8]<=0.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			return 'True'
		else: return 'True'
	elif obj[5]>20:
		return 'False'
	else: return 'False'
