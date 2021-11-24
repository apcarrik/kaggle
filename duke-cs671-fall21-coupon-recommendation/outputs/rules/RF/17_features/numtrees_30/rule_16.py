def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[10]<=9:
		# {"feature": "Coupon", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[3]>0:
			# {"feature": "Education", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[9]>0:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[14]<=1.0:
					return 'True'
				elif obj[14]>1.0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]<=0:
				# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]>3:
						return 'True'
					elif obj[6]<=3:
						return 'False'
					else: return 'False'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[10]>9:
		return 'False'
	else: return 'False'
